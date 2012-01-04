%global packname  fdth
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.5
Release:          1%{?dist}
Summary:          Frequency Distribution Tables, Histograms and Poligons

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-base R-grDevices R-graphics 

BuildRequires:    R-devel tex(latex) R-base R-grDevices R-graphics 

%description
Perform frequency distribution tables, associated histograms and poligons
from vector, data.frame and matrix objects.

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
%doc %{rlibdir}/fdth/DESCRIPTION
%doc %{rlibdir}/fdth/html
%{rlibdir}/fdth/R
%{rlibdir}/fdth/NAMESPACE
%{rlibdir}/fdth/help
%{rlibdir}/fdth/INDEX
%{rlibdir}/fdth/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.5-1
- initial package for Fedora