%global packname  trio
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.9
Release:          1%{?dist}
Summary:          Detection of disease-associated SNP interactions in case-parent trio data

Group:            Applications/Engineering 
License:          LGPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-haplo.stats 

BuildRequires:    R-devel tex(latex) R-survival R-haplo.stats 

%description
Testing SNPs and SNP interactions with a genotypic TDT. This package
furthermore contains functions for computing pairwise values of LD
measures and for identifying LD blocks, as well as functions for setting
up matched case pseudo-control genotype data for case-parent trios in
order to run trio logic regreesion, to impute missing genotypes in trios,
or to simulate case-parent trios with disease risk dependent on SNP

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
%doc %{rlibdir}/trio/html
%doc %{rlibdir}/trio/doc
%doc %{rlibdir}/trio/DESCRIPTION
%{rlibdir}/trio/data
%{rlibdir}/trio/plugin
%{rlibdir}/trio/NAMESPACE
%{rlibdir}/trio/help
%{rlibdir}/trio/Meta
%{rlibdir}/trio/R
RPM build errors:
%{rlibdir}/trio/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.9-1
- initial package for Fedora