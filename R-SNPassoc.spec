%global packname  SNPassoc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.1
Release:          1%{?dist}
Summary:          SNPs-based whole genome association studies

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-haplo.stats R-survival R-mvtnorm R-gdata 


BuildRequires:    R-devel tex(latex) R-haplo.stats R-survival R-mvtnorm R-gdata



%description
This package carries out most common analysis when performing whole genome
association studies. These analyses include descriptive statistics and
exploratory analysis of missing values, calculation of Hardy-Weinberg
equilibrium, analysis of association based on generalized linear models
(either for quantitative or binary traits), and analysis of multiple SNPs
(haplotype and epistasis analysis). Permutation test and related tests
(sum statistic and truncated product) are also implemented. Max-statistic
and genetic risk-allele score exact distributions are also possible to be

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.1-1
- initial package for Fedora