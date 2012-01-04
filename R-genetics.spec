%global packname  genetics
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.6
Release:          1%{?dist}
Summary:          Population Genetics

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-combinat R-gdata R-gtools R-MASS R-mvtnorm 


BuildRequires:    R-devel tex(latex) R-combinat R-gdata R-gtools R-MASS R-mvtnorm



%description
Classes and methods for handling genetic data. Includes classes to
represent genotypes and haplotypes at single markers up to multiple
markers on multiple chromosomes. Function include allele frequencies,
flagging homo/heterozygotes, flagging carriers of certain alleles,
estimating and testing for Hardy-Weinberg disequilibrium, estimating and
testing for linkage disequilibrium, ...

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.6-1
- initial package for Fedora