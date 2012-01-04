%global packname  MLInterfaces
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.34.0
Release:          1%{?dist}
Summary:          Uniform interfaces to R machine learning procedures for data in Bioconductor containers

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-MASS R-methods R-genefilter R-rpart R-rda R-annotate R-cluster R-sfsmisc 

BuildRequires:    R-devel tex(latex) R-Biobase R-MASS R-methods R-genefilter R-rpart R-rda R-annotate R-cluster R-sfsmisc 

%description
Uniform interfaces to machine learning code for data in Bioconductor

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.34.0-1
- initial package for Fedora