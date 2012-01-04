%global packname  codelink
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.22.0
Release:          1%{?dist}
Summary:          Manipulation of Codelink Bioarrays data.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase R-limma 
Requires:         R-annotate 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-limma
BuildRequires:    R-annotate 


%description
This packages allow reading into R of Codelink bioarray data exported as
text from the Codelink software. Also includes some functions to ease the
manipulation and pre-processing of data, such in background correction and

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.22.0-1
- initial package for Fedora