%global packname  pgfSweave
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Quality speedy graphics compilation and caching with Sweave

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stashR R-filehash R-highlight R-optparse R-formatR 
Requires:         R-digest R-tools R-utils R-tikzDevice R-cacheSweave 

BuildRequires:    R-devel tex(latex) R-stashR R-filehash R-highlight R-optparse R-formatR
BuildRequires:    R-digest R-tools R-utils R-tikzDevice R-cacheSweave 


%description
pgfSweave provides a number of improvements to the speed and quality of
Sweave output including: (1) capabilities for 'caching' graphics generated
with Sweave on top of the caching mechanisms provided by cacheSweave, (2)
an interface to the tikzDevice package which provides graphics with
consistent font style, sizing and quality as the main document and (3)
highlighting of echo'd source code via the highlight package. pgfSweave
provides a new driver for Sweave (pgfSweaveDriver) with new chunk options
tikz, external, sanitize, highlight and tidy on top of the cache option
provided by cacheSweave.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora