%global packname  minpack.lm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.5
Release:          1%{?dist}
Summary:          R interface to the Levenberg-Marquardt nonlinear least-squares algorithm found in MINPACK

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Provides R interface to lmder and lmdif from the MINPACK library, for
solving nonlinear least-squares problems by a modification of the
Levenberg-Marquardt algorithm.

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
%doc %{rlibdir}/minpack.lm/html
%doc %{rlibdir}/minpack.lm/DESCRIPTION
%{rlibdir}/minpack.lm/Meta
%{rlibdir}/minpack.lm/libs
%{rlibdir}/minpack.lm/NAMESPACE
%{rlibdir}/minpack.lm/R
%{rlibdir}/minpack.lm/INDEX
%{rlibdir}/minpack.lm/help
%{rlibdir}/minpack.lm/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.5-1
- initial package for Fedora