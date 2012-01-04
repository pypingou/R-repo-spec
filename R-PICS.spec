%global packname  PICS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          Probabilistic inference of ChIP-seq

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-IRanges R-GenomicRanges R-BSgenome 
Requires:         R-IRanges R-GenomicRanges R-BSgenome R-methods R-graphics R-grDevices R-stats 

BuildRequires:    R-devel tex(latex) R-IRanges R-GenomicRanges R-BSgenome
BuildRequires:    R-IRanges R-GenomicRanges R-BSgenome R-methods R-graphics R-grDevices R-stats 


%description
Probabilistic inference of ChIP-Seq using an empirical Bayes mixture model

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora