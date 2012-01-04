%global packname  exams
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Automatic Generation of Standardized Exams for Large-Lecture Courses

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-graphics R-tools R-utils 

BuildRequires:    R-devel tex(latex) R-stats R-graphics R-tools R-utils 

%description
Sweave-based automatic generation of exams with multiple-choice questions
and arithmetic problems.

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
%doc %{rlibdir}/exams/CITATION
%doc %{rlibdir}/exams/doc
%doc %{rlibdir}/exams/DESCRIPTION
%doc %{rlibdir}/exams/html
%doc %{rlibdir}/exams/NEWS
%{rlibdir}/exams/help
%{rlibdir}/exams/NAMESPACE
%{rlibdir}/exams/Meta
%{rlibdir}/exams/tex
%{rlibdir}/exams/INDEX
%{rlibdir}/exams/exercises
%{rlibdir}/exams/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora