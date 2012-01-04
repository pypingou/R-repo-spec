%global packname  tuneR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Analysis of music and speech

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-signal 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-signal 


%description
Collection of tools to analyze music, extract features like MFCCs,
handling wave files, read mp3, transcription, ... Also contains functions
ported from the rastamat Matlab package.

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
%doc %{rlibdir}/tuneR/CITATION
%doc %{rlibdir}/tuneR/DESCRIPTION
%doc %{rlibdir}/tuneR/html
%{rlibdir}/tuneR/Meta
%{rlibdir}/tuneR/NAMESPACE
%{rlibdir}/tuneR/libs
%{rlibdir}/tuneR/R
%{rlibdir}/tuneR/help
%{rlibdir}/tuneR/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.0-1
- initial package for Fedora