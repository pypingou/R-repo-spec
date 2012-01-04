%global packname  RNCBIEUtilsLibs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9
Release:          1%{?dist}
Summary:          EUtils libraries for use in the R environment.

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) R-rJava 

%description
Provides the libraries of the EUtils operations for the RNCBI package.

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
%doc %{rlibdir}/RNCBIEUtilsLibs/DESCRIPTION
%doc %{rlibdir}/RNCBIEUtilsLibs/html
%{rlibdir}/RNCBIEUtilsLibs/NAMESPACE
%{rlibdir}/RNCBIEUtilsLibs/Meta
%{rlibdir}/RNCBIEUtilsLibs/java
%{rlibdir}/RNCBIEUtilsLibs/INDEX
%{rlibdir}/RNCBIEUtilsLibs/R
%{rlibdir}/RNCBIEUtilsLibs/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9-1
- initial package for Fedora