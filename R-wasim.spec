%global packname  wasim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Visualisation and analysis of output files of the hydrological model WASIM

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-qualV R-tiger R-fast 


BuildRequires:    R-devel tex(latex) R-MASS R-qualV R-tiger R-fast



%description
Helpful tools for data processing and visualisation of results of the
hydrological model WASIM-ETH.

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
%doc %{rlibdir}/wasim/DESCRIPTION
%doc %{rlibdir}/wasim/html
%{rlibdir}/wasim/data
%{rlibdir}/wasim/Meta
%{rlibdir}/wasim/weisseritz
%{rlibdir}/wasim/NAMESPACE
%{rlibdir}/wasim/R
%{rlibdir}/wasim/INDEX
%{rlibdir}/wasim/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora