%global packname  Streamer
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Enabling stream processing of large files

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-methods R-graph 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-methods R-graph 


%description
Large data files can be difficult to work with in R, where data generally
resides in memory. This package encourages a style of programming where
data is 'streamed' from disk into R via a `producer' and through a series
of `consumers' that, typically reduce the original data to a manageable
size. The package provides useful Producer and Consumer stream components
for operations such as data input, sampling, indexing, and transformation;
see package?Streamer for details.

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
%doc %{rlibdir}/Streamer/html
%doc %{rlibdir}/Streamer/DESCRIPTION
%doc %{rlibdir}/Streamer/doc
%{rlibdir}/Streamer/unitTests
%{rlibdir}/Streamer/help
%{rlibdir}/Streamer/INDEX
%{rlibdir}/Streamer/Meta
%{rlibdir}/Streamer/libs
%{rlibdir}/Streamer/R
%{rlibdir}/Streamer/NAMESPACE
%{rlibdir}/Streamer/README-ncdf4.txt
%{rlibdir}/Streamer/scripts
%{rlibdir}/Streamer/extdata

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora