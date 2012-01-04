%global packname  proxy
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.7
Release:          1%{?dist}
Summary:          Distance and Similarity Measures

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Provides an extensible framework for the effcient calculation of auto- and
cross-proximities, along with implementations of the most popular ones.

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
%doc %{rlibdir}/proxy/NEWS
%doc %{rlibdir}/proxy/DESCRIPTION
%doc %{rlibdir}/proxy/doc
%doc %{rlibdir}/proxy/html
%{rlibdir}/proxy/libs
%{rlibdir}/proxy/help
%{rlibdir}/proxy/NAMESPACE
%{rlibdir}/proxy/Meta
%{rlibdir}/proxy/INDEX
%{rlibdir}/proxy/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.7-1
- initial package for Fedora