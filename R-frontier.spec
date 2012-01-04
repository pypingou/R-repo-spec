%global packname  frontier
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.997.2
Release:          1%{?dist}
Summary:          Stochastic Frontier Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.997-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-plm R-micEcon R-miscTools R-Formula R-lmtest 
Requires:         R-moments 

BuildRequires:    R-devel tex(latex) R-plm R-micEcon R-miscTools R-Formula R-lmtest
BuildRequires:    R-moments 


%description
Maximum Likelihood Estimation of Stochastic Frontier Production and Cost
Functions. Two specifications are available: the error components
specification with time-varying efficiencies (Battese and Coelli, 1992)
and a model specification in which the firm effects are directly
influenced by a number of variables (Battese and Coelli, 1995).

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.997.2-1
- initial package for Fedora