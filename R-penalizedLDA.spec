%global packname  penalizedLDA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Penalized classification using Fisher's linear discriminant

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-flsa 

BuildRequires:    R-devel tex(latex) R-flsa 

%description
Implements the penalized LDA proposal of "Witten and Tibshirani (2011),
Penalized classification using Fisher's linear discriminant, to appear in
Journal of the Royal Statistical Society, Series B".

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
%doc %{rlibdir}/penalizedLDA/html
%doc %{rlibdir}/penalizedLDA/DESCRIPTION
%{rlibdir}/penalizedLDA/INDEX
%{rlibdir}/penalizedLDA/R
%{rlibdir}/penalizedLDA/NAMESPACE
%{rlibdir}/penalizedLDA/help
%{rlibdir}/penalizedLDA/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora