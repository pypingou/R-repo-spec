%global packname  rtfbs
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          R Transcription Factor Binding Site identification tool

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-rphast 

BuildRequires:    R-devel tex(latex) R-stats R-rphast 

%description
RTFBS identifies and scores possible Transcription Factor Binding Sites
and allows for FDR analysis and pruning.  It supports splitting of
sequences based on size or a specified GFF, grouping by GC content, and
specification of Markov model order.  The heavy lifting is done in C while
all results are made available via R.

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
%doc %{rlibdir}/rtfbs/doc
%doc %{rlibdir}/rtfbs/DESCRIPTION
%doc %{rlibdir}/rtfbs/html
%{rlibdir}/rtfbs/extdata
%{rlibdir}/rtfbs/INDEX
%{rlibdir}/rtfbs/help
%{rlibdir}/rtfbs/NAMESPACE
%{rlibdir}/rtfbs/R
%{rlibdir}/rtfbs/Meta
RPM build errors:
%{rlibdir}/rtfbs/libs

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora