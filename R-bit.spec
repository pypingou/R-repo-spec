%global packname  bit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.7
Release:          1%{?dist}
Summary:          A class for vectors of 1-bit booleans

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
bitmapped vectors of booleans (no NAs), coercion from and to logicals,
integers and integer subscripts; fast boolean operators and fast summary
statistics. With 'bit' vectors you can store true binary booleans
{FALSE,TRUE} at the expense of 1 bit only, on a 32 bit architecture this
means factor 32 less RAM and ~ factor 32 more speed on boolean operations.
Due to overhead of R calls, actual speed gain depends on the size of the
vector: expect gains for vectors of size > 10000 elements. Even for
one-time boolean operations it can pay-off to convert to bit, the pay-off
is obvious, when such components are used more than once. Reading from and
writing to bit is approximately as fast as accessing standard logicals -
mostly due to R's time for memory allocation. The package allows to work
with pre-allocated memory for return values by calling .Call() directly:
when evaluating the speed of C-access with pre-allocated vector memory,
coping from bit to logical requires only 70% of the time for copying from
logical to logical; and copying from logical to bit comes at a performance
penalty of 150%. the package now contains further classes for representing
logical selections: 'bitwhich' for very skewed selections and 'ri' for
selecting ranges of values for chunked processing. All three index classes
can be used for subsetting 'ff' objects (ff-2.1-0 and higher).

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.7-1
- initial package for Fedora