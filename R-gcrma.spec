%global packname  gcrma
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.26.0
Release:          1%{?dist}
Summary:          Background Adjustment Using Sequence Information

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-affy R-graphics R-methods R-stats R-utils 
Requires:         R-Biobase R-affy R-affyio R-IRanges R-Biostrings R-splines 

BuildRequires:    R-devel tex(latex) R-affy R-graphics R-methods R-stats R-utils
BuildRequires:    R-Biobase R-affy R-affyio R-IRanges R-Biostrings R-splines 


%description
Background adjustment using sequence information

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.26.0-1
- initial package for Fedora