%global packname  colorspace
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Color Space Manipulation

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Carries out mapping between assorted color spaces including RGB, HSV, HLS,
CIEXYZ, CIELUV, HCL (polar CIELUV), CIELAB and polar CIELAB. Qualitative,
sequential, and diverging color palettes based on HCL colors are provided.

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
%doc %{rlibdir}/colorspace/DESCRIPTION
%doc %{rlibdir}/colorspace/CITATION
%doc %{rlibdir}/colorspace/html
%doc %{rlibdir}/colorspace/NEWS
%{rlibdir}/colorspace/INDEX
%{rlibdir}/colorspace/doc
%{rlibdir}/colorspace/help
%{rlibdir}/colorspace/NAMESPACE
%{rlibdir}/colorspace/R
%{rlibdir}/colorspace/libs
%{rlibdir}/colorspace/Meta

%changelog
* Sat Feb 11 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- Update to 1.1.1

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora
