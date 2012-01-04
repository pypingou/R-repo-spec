%global packname  RArcInfo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.12
Release:          1%{?dist}
Summary:          Functions to import data from Arc/Info V7.x binary coverages

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RColorBrewer 

BuildRequires:    R-devel tex(latex) R-RColorBrewer 

%description
This package uses the functions written by Daniel Morissette
<danmo@videotron.ca> to read geographical information in Arc/Info V 7.x
format and E00 files to import the coverages into R variables.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.12-1
- initial package for Fedora