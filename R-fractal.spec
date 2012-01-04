%global packname  fractal
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Fractal Time Series Modeling and Analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-splus2R R-ifultools R-sapa R-wmtsa R-akima R-MASS R-scatterplot3d 

BuildRequires:    R-devel tex(latex) R-splus2R R-ifultools R-sapa R-wmtsa R-akima R-MASS R-scatterplot3d 

%description
Stochastic fractal and deterministic chaotic time series analysis.

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
%doc %{rlibdir}/fractal/html
%doc %{rlibdir}/fractal/DESCRIPTION
%{rlibdir}/fractal/Meta
%{rlibdir}/fractal/INDEX
%{rlibdir}/fractal/bookexams
%{rlibdir}/fractal/NAMESPACE
%{rlibdir}/fractal/help
%{rlibdir}/fractal/R
%{rlibdir}/fractal/fractal.chm

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora