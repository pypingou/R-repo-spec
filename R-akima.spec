%global packname  akima
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.7
Release:          1%{?dist}
Summary:          Interpolation of irregularly spaced data

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Linear or cubic spline interpolation for irregular gridded data

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
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE


%changelog
* Mon Jan 30 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.5.7-1
- fix files
- update to upstream release 0.5.7

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.4-1
- initial package for Fedora
