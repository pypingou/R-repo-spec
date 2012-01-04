%global packname  MuMIn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.1
Release:          1%{?dist}
Summary:          Multi-model inference

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Model selection and model averaging based on information criteria (AICc
and alike).

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
%doc %{rlibdir}/MuMIn/html
%doc %{rlibdir}/MuMIn/NEWS
%doc %{rlibdir}/MuMIn/DESCRIPTION
%doc %{rlibdir}/MuMIn/doc
%{rlibdir}/MuMIn/data
%{rlibdir}/MuMIn/INDEX
%{rlibdir}/MuMIn/NAMESPACE
%{rlibdir}/MuMIn/help
%{rlibdir}/MuMIn/Meta
%{rlibdir}/MuMIn/R
%{rlibdir}/MuMIn/TODO

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.1-1
- initial package for Fedora