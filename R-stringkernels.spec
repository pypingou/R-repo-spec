%global packname  stringkernels
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.9
Release:          1%{?dist}
Summary:          String Kernel Methods for kernlab

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-kernlab R-openNLP 


BuildRequires:    R-devel tex(latex) R-methods R-kernlab R-openNLP



%description
Gapped and word-based string kernels for use with kernlab

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.9-1
- initial package for Fedora