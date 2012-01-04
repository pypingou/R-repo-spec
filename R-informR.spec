%global packname  informR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.01
Release:          1%{?dist}
Summary:          informR: R Tools for Creating Sequence Statistics

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-abind R-relevent 

BuildRequires:    R-devel tex(latex) R-abind R-relevent 

%description
Tools for creating sequence statistics, especially for Butts's egocentric
relational event model fitting software in the relevent R package

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.01-1
- initial package for Fedora