%global packname  R4dfp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          4dfp MRI Image Read and Write Routines

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides an R interface with 2-part 4dfp MRI images
(.4dfp.ifh and .4dfp.img files.)

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
%doc %{rlibdir}/R4dfp/DESCRIPTION
%doc %{rlibdir}/R4dfp/html
%{rlibdir}/R4dfp/libs
%{rlibdir}/R4dfp/help
%{rlibdir}/R4dfp/NAMESPACE
%{rlibdir}/R4dfp/Meta
%{rlibdir}/R4dfp/INDEX
%{rlibdir}/R4dfp/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.9-1
- initial package for Fedora