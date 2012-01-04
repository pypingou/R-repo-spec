%global packname  infoDecompuTE
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Information Decomposition of Two-phase Experiments

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
InfoDecompuTE is capable of generating the structure of the analysis of
variance (ANOVA) table of the two-phase experiments. By inputting the
design and the relationships of the random and fixed factors using the
Wilkinson-Rogers' syntax, infoDecompuTE can generate the structure of the
ANOVA table with the coefficients of the variance components for the
expected mean squares. This package can also study the balanced incomplete
block design and provides the efficiency factors of the fixed effects.

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
%doc %{rlibdir}/infoDecompuTE/DESCRIPTION
%doc %{rlibdir}/infoDecompuTE/html
%{rlibdir}/infoDecompuTE/INDEX
%{rlibdir}/infoDecompuTE/NAMESPACE
%{rlibdir}/infoDecompuTE/help
%{rlibdir}/infoDecompuTE/R
%{rlibdir}/infoDecompuTE/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.3-1
- initial package for Fedora