%global packname  qualV
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Qualitative Validation Methods

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-KernSmooth 

BuildRequires:    R-devel tex(latex) R-KernSmooth 

%description
Qualitative methods for the validation of models.

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
%doc %{rlibdir}/qualV/DESCRIPTION
%doc %{rlibdir}/qualV/CITATION
%doc %{rlibdir}/qualV/html
%doc %{rlibdir}/qualV/NEWS
%{rlibdir}/qualV/THANKS
%{rlibdir}/qualV/demo
%{rlibdir}/qualV/NAMESPACE
%{rlibdir}/qualV/INDEX
%{rlibdir}/qualV/help
%{rlibdir}/qualV/Meta
%{rlibdir}/qualV/data
%{rlibdir}/qualV/R
%{rlibdir}/qualV/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora