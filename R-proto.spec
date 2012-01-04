%global packname  proto
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.9.2
Release:          1%{?dist}
Summary:          Prototype object-based programming

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-9.2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
An object oriented system using object-based, also called prototype-based,
rather than class-based object oriented ideas.

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
%doc %{rlibdir}/proto/html
%doc %{rlibdir}/proto/NEWS
%doc %{rlibdir}/proto/DESCRIPTION
%doc %{rlibdir}/proto/doc
%{rlibdir}/proto/README
%{rlibdir}/proto/WISHLIST
%{rlibdir}/proto/FAQ
%{rlibdir}/proto/help
%{rlibdir}/proto/INDEX
%{rlibdir}/proto/THANKS
%{rlibdir}/proto/demo
%{rlibdir}/proto/Meta
%{rlibdir}/proto/NAMESPACE
%{rlibdir}/proto/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.9.2-1
- initial package for Fedora