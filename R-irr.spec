%global packname  irr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.83
Release:          1%{?dist}
Summary:          Various Coefficients of Interrater Reliability and Agreement

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lpSolve 

BuildRequires:    R-devel tex(latex) R-lpSolve 

%description
Coefficients of Interrater Reliability and Agreement for quantitative,
ordinal and nominal data: ICC, Finn-Coefficient, Robinson'A, Kendall's W,
Cohen's Kappa, ...

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
%doc %{rlibdir}/irr/html
%doc %{rlibdir}/irr/DESCRIPTION
%{rlibdir}/irr/Meta
%{rlibdir}/irr/INDEX
%{rlibdir}/irr/R
%{rlibdir}/irr/help
%{rlibdir}/irr/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.83-1
- initial package for Fedora