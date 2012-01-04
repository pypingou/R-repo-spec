%global packname  DEXSeq
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Inference of differential exon usage in RNA-Seq

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase 
Requires:         R-hwriter R-methods R-stringr R-statmod 

BuildRequires:    R-devel tex(latex) R-Biobase
BuildRequires:    R-hwriter R-methods R-stringr R-statmod 


%description
The package is focused on finding differential exon usage using RNA-seq
exon counts between samples with different experimental designs. It
provides functions that allows the user to make the necessary statistical
tests based on a model that uses the negative binomial distribution to
estimate the variance between biological replicates and generalized linear
models for testing. The package also provides functions for the
visualization and exploration of the results.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora