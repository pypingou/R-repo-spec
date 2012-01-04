%global packname  MultiPhen
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          MultiPhen, a package for the genetic association testing of multiple phenotypes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-abind R-epitools R-meta 

BuildRequires:    R-devel tex(latex) R-MASS R-abind R-epitools R-meta 

%description
Performs genetic association tests between SNPs (one-at-a-time) and
multiple phenotypes (separately or in joint model)

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
%doc %{rlibdir}/MultiPhen/html
%doc %{rlibdir}/MultiPhen/DESCRIPTION
%{rlibdir}/MultiPhen/INDEX
%{rlibdir}/MultiPhen/R
%{rlibdir}/MultiPhen/data
%{rlibdir}/MultiPhen/help
%{rlibdir}/MultiPhen/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora