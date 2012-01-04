%global packname  KrigInv
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Kriging-based Inversion for Deterministic and Noisy Computer Experiments

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-DiceKriging R-rgenoud R-MASS R-lhs 

BuildRequires:    R-devel tex(latex) R-DiceKriging R-rgenoud R-MASS R-lhs 

%description
Criteria and algorithms for sequentially estimating level sets of a
multivariate numerical function, possibly observed in tunable noise.

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
%doc %{rlibdir}/KrigInv/html
%doc %{rlibdir}/KrigInv/DESCRIPTION
%{rlibdir}/KrigInv/help
%{rlibdir}/KrigInv/R
%{rlibdir}/KrigInv/NAMESPACE
%{rlibdir}/KrigInv/INDEX
%{rlibdir}/KrigInv/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora