%global packname  LaF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Fast access to large ASCII files

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcpp R-methods 


BuildRequires:    R-devel tex(latex) R-Rcpp R-methods



%description
The LaF package provides methods for fast access to large ASCII files. 
Currently the following file formats are supported: comma separated format
(csv) and fixed width format. It is assumed that the files are too large
to fit into memory, although the package can also be used to efficiently
access files that do fit into memory. Methods are provided to access and
process files blockwise. Furthermore, an opened file can be accessed as
one would an ordinary data.frame. The LaF vignette gives an overview of
the functionality provided.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora