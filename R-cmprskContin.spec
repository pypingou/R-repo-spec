%global packname  cmprskContin
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Continuous mark-specific relative risks for two groups

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Estimation and testing of continuous mark-specific relative risks in two
groups as described in Gilbert, P., McKeague, I. and Sun, Y. (2008) The
2-sample problem for failure rates depending on a continuous mark: an
application to vaccine efficacy. Biostatistics 9, 2, 263-276. This package
implements the methods presented in the paper for testing mark-specific
hazards ratios and for estimation of mark-specific incidence ratios that
are cumulative in time or cumulative in both time and the continuous mark.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7-1
- initial package for Fedora