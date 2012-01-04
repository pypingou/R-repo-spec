%global packname  trex
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Truncated exact test for two-stage case-control design for studying rare genetic variants

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The first stage is screening to detect rare variants in only cases. If the
number of case-carriers of any rare variants exceeds a user-specified
threshold, then additional cases and controls are genotyped for the
detected variants and carrier status of these variants are compared for
all cases and controls in the second stage. The package includes two main
functions, trex for the exact test and optimalDesign to determine
potential two-stage designs including an optimal design.

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
%doc %{rlibdir}/trex/doc
%doc %{rlibdir}/trex/html
%doc %{rlibdir}/trex/DESCRIPTION
%{rlibdir}/trex/INDEX
%{rlibdir}/trex/help
%{rlibdir}/trex/LICENSE
%{rlibdir}/trex/NAMESPACE
%{rlibdir}/trex/Meta
%{rlibdir}/trex/R
%{rlibdir}/trex/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora