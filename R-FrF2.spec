%global packname  FrF2
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.10
Release:          1%{?dist}
Summary:          Fractional Factorial designs with 2-level factors

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-BsMD R-scatterplot3d R-igraph R-DoE.base 
Requires:         R-sfsmisc 

BuildRequires:    R-devel tex(latex) R-BsMD R-scatterplot3d R-igraph R-DoE.base
BuildRequires:    R-sfsmisc 


%description
This package creates regular and non-regular Fractional Factorial designs.
Furthermore, analysis tools for Fractional Factorial designs with 2-level
factors are offered (main effects and interaction plots for all factors
simultaneously, cube plot for looking at the simultaneous effects of three
factors, full or half normal plot, alias structure in a more readable
format than with the built-in function alias). The package is currently
subject to intensive development. While much of the intended functionality
is already available, some changes and improvements are still to be
expected. Suggestions are welcome.

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
%doc %{rlibdir}/FrF2/NEWS
%doc %{rlibdir}/FrF2/DESCRIPTION
%doc %{rlibdir}/FrF2/html
%{rlibdir}/FrF2/NAMESPACE
%{rlibdir}/FrF2/LICENSE
%{rlibdir}/FrF2/INDEX
%{rlibdir}/FrF2/R
%{rlibdir}/FrF2/help
%{rlibdir}/FrF2/Meta

%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.10-1
- initial package for Fedora