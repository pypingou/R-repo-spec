%global packname  scriptests
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Transcript-based unit tests that are easy to create and maintain

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Support for using .Rt (transcript) tests in the tests directory of a
package.  Provides more convenience and features than the standard
.R/.Rout.save tests.  Tests can be run under R CMD check and also
interactively.  Provides source.pkg() for quickly loading code, DLLs, and
data from a package for use in an edit/compile/test development cycle.

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
%doc %{rlibdir}/scriptests/NEWS
%doc %{rlibdir}/scriptests/html
%doc %{rlibdir}/scriptests/doc
%doc %{rlibdir}/scriptests/DESCRIPTION
%{rlibdir}/scriptests/examples
%{rlibdir}/scriptests/R
%{rlibdir}/scriptests/NAMESPACE
%{rlibdir}/scriptests/Meta
%{rlibdir}/scriptests/help
%{rlibdir}/scriptests/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora