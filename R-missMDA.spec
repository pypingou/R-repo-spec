%global packname  missMDA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Handling missing values with/in multivariate data analysis (principal component methods)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-FactoMineR 

BuildRequires:    R-devel tex(latex) R-FactoMineR 

%description
Imputation of incomplete continuous or categorical datasets; Missing
values are imputed with a principal component analysis (PCA), a multiple
correspondence analysis (MCA) model or a multiple factor analysis (MFA)
model; Perform multiple imputation with and in PCA

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
%doc %{rlibdir}/missMDA/html
%doc %{rlibdir}/missMDA/DESCRIPTION
%{rlibdir}/missMDA/data
%{rlibdir}/missMDA/help
%{rlibdir}/missMDA/INDEX
%{rlibdir}/missMDA/R
%{rlibdir}/missMDA/Meta

%changelog
* Wed Nov 23 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora