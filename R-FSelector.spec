%global packname  FSelector
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.18
Release:          1%{?dist}
Summary:          Selecting attributes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-randomForest R-RWeka R-digest 


BuildRequires:    R-devel tex(latex) R-randomForest R-RWeka R-digest



%description
This package provides functions for selecting attributes from a given
dataset. Attribute subset selection is the process of identifying and
removing as much of the irrevelant and redundant information as possible.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.18-1
- initial package for Fedora