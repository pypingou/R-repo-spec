%global packname  hapassoc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          Inference of trait associations with SNP haplotypes and other attributes using the EM Algorithm

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
The following R functions are used for inference of trait associations
with haplotypes and other covariates in generalized linear models.  The
functions are developed primarily for data collected in cohort or
cross-sectional studies. They can accommodate uncertain haplotype phase
and handle missing genotypes at some SNPs.

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
%doc %{rlibdir}/hapassoc/html
%doc %{rlibdir}/hapassoc/DESCRIPTION
%doc %{rlibdir}/hapassoc/doc
%doc %{rlibdir}/hapassoc/CITATION
%{rlibdir}/hapassoc/NAMESPACE
%{rlibdir}/hapassoc/Meta
%{rlibdir}/hapassoc/R
%{rlibdir}/hapassoc/INDEX
%{rlibdir}/hapassoc/ChangeLog
%{rlibdir}/hapassoc/data
%{rlibdir}/hapassoc/help
%{rlibdir}/hapassoc/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.4-1
- initial package for Fedora