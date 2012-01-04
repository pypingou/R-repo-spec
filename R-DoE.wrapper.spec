%global packname  DoE.wrapper
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.6
Release:          1%{?dist}
Summary:          Wrapper package for design of experiments functionality

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-FrF2 R-DoE.base R-rsm R-lhs R-DiceDesign R-AlgDesign 


BuildRequires:    R-devel tex(latex) R-FrF2 R-DoE.base R-rsm R-lhs R-DiceDesign R-AlgDesign



%description
This package creates various kinds of designs for (industrial)
experiments. It uses, and sometimes enhances, design generation routines
from other packages. So far, response surface designs from package rsm,
latin hypercube samples from packages lhs and DiceDesign, and D-optimal
designs from package AlgDesign have been implemented.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.6-1
- initial package for Fedora