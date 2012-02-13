%global packname  DiceOptim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{dist}
Summary:          Kriging-based optimization for computer experiments

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-DiceKriging R-rgenoud R-MASS 

BuildRequires:    R-devel tex(latex) R-DiceKriging R-rgenoud R-MASS 

%description
Expected Improvement. EGO algorithm. Parallelized versions of EGO:
Constant Liars.

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
%doc %{rlibdir}/DiceOptim/html
%doc %{rlibdir}/DiceOptim/DESCRIPTION
%{rlibdir}/DiceOptim/INDEX
%{rlibdir}/DiceOptim/help
%{rlibdir}/DiceOptim/data
%{rlibdir}/DiceOptim/NAMESPACE
%{rlibdir}/DiceOptim/R
%{rlibdir}/DiceOptim/Meta

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- Update to version 1.2.1

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora