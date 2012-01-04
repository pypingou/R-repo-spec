%global packname  RKEA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          R/KEA interface

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-rJava R-tm 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-rJava R-tm 


%description
An R interface to KEA (Version 5.0). KEA (for Keyphrase Extraction
Algorithm) allows for extracting keyphrases from text documents. It can be
either used for free indexing or for indexing with a controlled
vocabulary. For more information see http://www.nzdl.org/Kea/.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.3-1
- initial package for Fedora