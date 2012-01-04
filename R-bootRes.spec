%global packname  bootRes
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Bootstrapped Response and Correlation Functions

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-base R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-base R-stats R-utils 

%description
Calculation of Bootstrapped Response and Correlation Functions for Use in

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
%doc %{rlibdir}/bootRes/DESCRIPTION
%doc %{rlibdir}/bootRes/html
%{rlibdir}/bootRes/INDEX
%{rlibdir}/bootRes/help
%{rlibdir}/bootRes/Meta
%{rlibdir}/bootRes/data
%{rlibdir}/bootRes/R
%{rlibdir}/bootRes/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora