%global packname  Rlab
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.9.0
Release:          1%{?dist}
Summary:          Functions and Datasets Required for ST370 class

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
Functions and Datasets Required for ST370 class

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
%doc %{rlibdir}/Rlab/html
%doc %{rlibdir}/Rlab/DESCRIPTION
%{rlibdir}/Rlab/R
%{rlibdir}/Rlab/help
%{rlibdir}/Rlab/INDEX
%{rlibdir}/Rlab/NAMESPACE
%{rlibdir}/Rlab/data
%{rlibdir}/Rlab/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.9.0-1
- initial package for Fedora