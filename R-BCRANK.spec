%global packname  BCRANK
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.16.0
Release:          1%{?dist}
Summary:          Predicting binding site consensus from ranked DNA sequences

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-Biostrings 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-Biostrings 


%description
Functions and classes for de novo prediction of transcription factor
binding consensus by heuristic search

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
%doc %{rlibdir}/BCRANK/DESCRIPTION
%doc %{rlibdir}/BCRANK/doc
%doc %{rlibdir}/BCRANK/html
%{rlibdir}/BCRANK/help
%{rlibdir}/BCRANK/R
%{rlibdir}/BCRANK/INDEX
%{rlibdir}/BCRANK/Exfiles
%{rlibdir}/BCRANK/NAMESPACE
%{rlibdir}/BCRANK/libs
%{rlibdir}/BCRANK/data
%{rlibdir}/BCRANK/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.0-1
- initial package for Fedora