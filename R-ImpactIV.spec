%global packname  ImpactIV
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Identifying Causal Effect for Multi-Component Intervention Using Instrumental Variable Method

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nnet 

BuildRequires:    R-devel tex(latex) R-nnet 

%description
In this package, you can find two functions proposed in Ding, Geng and
Zhou (2011) to estimate direct and indirect causal effects with
randomization and multiple-component intervention using instrumental
variable method.

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
%doc %{rlibdir}/ImpactIV/DESCRIPTION
%doc %{rlibdir}/ImpactIV/html
%{rlibdir}/ImpactIV/data
%{rlibdir}/ImpactIV/R
%{rlibdir}/ImpactIV/NAMESPACE
%{rlibdir}/ImpactIV/INDEX
%{rlibdir}/ImpactIV/help
%{rlibdir}/ImpactIV/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora