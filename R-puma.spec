%global packname  puma
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.6.0
Release:          1%{?dist}
Summary:          Propagating Uncertainty in Microarray Analysis

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-affy R-graphics R-grDevices R-methods R-stats R-utils R-mclust 
Requires:         R-Biobase R-affy 

BuildRequires:    R-devel tex(latex) R-Biobase R-affy R-graphics R-grDevices R-methods R-stats R-utils R-mclust
BuildRequires:    R-Biobase R-affy 


%description
Most analyses of Affymetrix GeneChip data are based on point estimates of
expression levels and ignore the uncertainty of such estimates. By
propagating uncertainty to downstream analyses we can improve results from
microarray analyses. For the first time, the puma package makes a suite of
uncertainty propagation methods available to a general audience. puma also
offers improvements in terms of scope and speed of execution over
previously available uncertainty propagation methods. Included are
summarisation, differential expression detection, clustering and PCA
methods, together with useful plotting and data manipulation functions.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6.0-1
- initial package for Fedora