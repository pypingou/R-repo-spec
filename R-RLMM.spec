%global packname  RLMM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.16.0
Release:          1%{?dist}
Summary:          A Genotype Calling Algorithm for Affymetrix SNP Arrays

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A classification algorithm, based on a multi-chip, multi-SNP approach for
Affymetrix SNP arrays. Using a large training sample where the genotype
labels are known, this aglorithm will obtain more accurate classification
results on new data. RLMM is based on a robust, linear model and uses the
Mahalanobis distance for classification. The chip-to-chip non-biological
variation is removed through normalization. This model-based algorithm
captures the similarities across genotype groups and probes, as well as
thousands other SNPs for accurate classification. NOTE: 100K-Xba only at
for now.

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
%doc %{rlibdir}/RLMM/html
%doc %{rlibdir}/RLMM/DESCRIPTION
%doc %{rlibdir}/RLMM/doc
%{rlibdir}/RLMM/Meta
%{rlibdir}/RLMM/INDEX
%{rlibdir}/RLMM/R
%{rlibdir}/RLMM/NAMESPACE
%{rlibdir}/RLMM/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.0-1
- initial package for Fedora