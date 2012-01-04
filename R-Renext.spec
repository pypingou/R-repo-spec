%global packname  Renext
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Renewal method for extreme values extrapolation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
R package dedicated to some Extreme values problems and allowing the use
of the so-called "renewal method" which is popular among french-speaking

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
%doc %{rlibdir}/Renext/html
%doc %{rlibdir}/Renext/DESCRIPTION
%doc %{rlibdir}/Renext/doc
%{rlibdir}/Renext/Meta
%{rlibdir}/Renext/NAMESPACE
%{rlibdir}/Renext/R
%{rlibdir}/Renext/Rendata
%{rlibdir}/Renext/help
%{rlibdir}/Renext/INDEX
%{rlibdir}/Renext/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora