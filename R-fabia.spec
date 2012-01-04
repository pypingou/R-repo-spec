%global packname  fabia
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          FABIA: Factor Analysis for Bicluster Acquisition

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Biclustering by "Factor Analysis for Bicluster Acquisition" (FABIA). FABIA
is a model-based technique for biclustering, that is clustering rows and
columns simultaneously. Biclusters are found by factor analysis where both
the factors and the loading matrix are sparse. FABIA is a multiplicative
model that extracts linear dependencies between samples and feature
patterns. It captures realistic non-Gaussian data distributions with heavy
tails as observed in gene expression measurements. FABIA utilizes well
understood model selection techniques like the EM algorithm and
variational approaches and is embedded into a Bayesian framework. FABIA
ranks biclusters according to their information content and separates
spurious biclusters from true biclusters. The code is written in C.

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
%doc %{rlibdir}/fabia/html
%doc %{rlibdir}/fabia/LICENCE
%doc %{rlibdir}/fabia/doc
%doc %{rlibdir}/fabia/NEWS
%doc %{rlibdir}/fabia/CITATION
%doc %{rlibdir}/fabia/DESCRIPTION
%{rlibdir}/fabia/demo
%{rlibdir}/fabia/NAMESPACE
%{rlibdir}/fabia/INDEX
%{rlibdir}/fabia/help
%{rlibdir}/fabia/Meta
%{rlibdir}/fabia/R
%{rlibdir}/fabia/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.0-1
- initial package for Fedora