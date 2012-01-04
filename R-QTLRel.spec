%global packname  QTLRel
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.10
Release:          1%{?dist}
Summary:          Tools for mapping of quantitative traits of genetically related individuals and calculating identity coefficients from a pedigree

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-gdata 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-gdata 


%description
This software provides tools for quantitative trait mapping in populations
such as advanced intercross lines where relatedness among individuals
should not be ignored. It can estimate background genetic variance
components, impute missing genotypes, simulate genotypes, perform a genome
scan for putative quantitative trait loci (QTL), and plot mapping results.
It also has functions to calculate identity coefficients from pedigrees,
especially suitable for pedigrees that consist of a large number of
generations, or estimate identity coefficients from genotypic data in
certain circumstances.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.10-1
- initial package for Fedora